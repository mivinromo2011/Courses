import java.io.*;
import java.util.*;

public class maximalMunch implements Scanner{
    /**
    Variables:
		*Current-state
		*Last final state
		*Current Input position
		*Last final input position
		*Begin-token position
	Methods:
		*Next token
		*next char
     */
	int curState;
	int curInputPos;

	int lastFinalState;
	int lastFinalInputPos;

	DFA dfa;
	String inp;
	String lexeme;
	Stack< int[]> stack;
	boolean[][] failed;
	char curInputChar;
	
	public maximalMunch(String input, DFA dfa) {
        this.inp = input;
		this.stack = new Stack<>();
		this.dfa = dfa;
		this.failed = new boolean[this.dfa.getNumberOfStates()][input.length()];
		initializeScanner();
    }

	private void initializeScanner(){
		curInputPos = -1;
		for(int i = 0; i< failed.length; i++){
			for(int j = 0; j<failed[i].length; j++){
				failed[i][j] = false;
			}
		}
	}
	
	public boolean reachedEOS(){
        return this.curInputPos == this.inp.length()-1;
	}
	
	public String nextToken(){
		this.curState = 1;
		this.lexeme = "";
		this.stack.clear();
		this.stack.push(new int[] {-10,-10});
		while((this.curState != -1) && (!reachedEOS())){
			this.curInputPos +=1;
			nextChar();
			//this.curInputPos +=1;
			lexeme = lexeme + curInputChar;
			if(failed[curState-1][curInputPos]){
				break;
			}
			if(this.dfa.tokenTable.containsKey(this.curState)){
                this.stack.clear();
			}
			this.stack.push(new int[] {curState,curInputPos});
			int cat = this.dfa.charCat.get(String.valueOf(this.curInputChar));
			this.curState = this.dfa.getTransition(this.curState-1, cat);
		}

		//Clean up final state and update the table
		while(!this.dfa.tokenTable.containsKey(this.curState) && curState != -10){
			if(this.curState == -1){
				this.failed[failed.length-1][curInputPos] = true;
			}
			else{
				this.failed[curState-1][curInputPos] = true;
			}

			int[] temp = this.stack.pop();
			this.curState = temp[0];
			this.curInputPos = temp[1];

			//truncate lexeme
			if(this.lexeme.length()>1){
				this.lexeme= this.lexeme.substring(0,lexeme.length()-1);
			}
			rollback();
		}

		if(this.dfa.tokenTable.containsKey(this.curState)){
            return this.dfa.getToken(this.curState);
        }
        else{
            return "Invalid";
        }
	}
	public void nextChar(){
		this.curInputChar = inp.charAt(this.curInputPos);
	}

	public void rollback(){
        this.curInputPos -=1;
	}
	
	/**private class intPair{
		int state;
		int inputPos;
		intPair(int state, int inputPos){
			this.state = state;
			this.inputPos = inputPos;
		}
	}*/
}