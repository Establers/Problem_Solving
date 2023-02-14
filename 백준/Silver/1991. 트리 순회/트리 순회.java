import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class TreeNode{
	char data;
	TreeNode left;
	TreeNode right;
	
	TreeNode(){};
	TreeNode(char c){
		data = c;
	}
	public TreeNode(char data, TreeNode left, TreeNode right) {
		super();
		this.data = data;
		this.left = left;
		this.right = right;
	}
	
}

public class Main {
	static int N;
	static List<TreeNode> binaryTree;
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		binaryTree = new ArrayList<>();
		
		//트리 'A'부터 'A'+N까지 노드 생성 후 > 리스트
		for(char c='A';c-'A'<N;c++) {
			TreeNode node = new TreeNode(c,null,null);
			binaryTree.add(node);
		}

		//노드끼리 연결
		for(int i=0;i<N;i++) {
			char data, l, r;
			st= new StringTokenizer(br.readLine());
			data = st.nextToken().charAt(0);
			l = st.nextToken().charAt(0);
			r = st.nextToken().charAt(0);
			if(l!='.') binaryTree.get(data - 'A').left = binaryTree.get(l - 'A');
			if(r!='.') binaryTree.get(data - 'A').right = binaryTree.get(r - 'A');
		}
		
		/*
		//확인용 출력문
		for(int i=0;i<N;i++) {
			System.out.println("node " + binaryTree.get(i).data
					+ " left "+ (binaryTree.get(i).left!=null?binaryTree.get(i).left.data:' ')
						+" right : "+ (binaryTree.get(i).right!=null? binaryTree.get(i).right.data:' '));
			
		}
		*/
		preOrder(binaryTree.get(0));
		bw.newLine(); bw.flush();
		inOrder(binaryTree.get(0));
		bw.newLine(); bw.flush();
		postOrder(binaryTree.get(0));
		bw.flush();
		
		
	} //Main 종료

	static void preOrder(TreeNode T) throws IOException { //전위 (중 좌 우)
		bw.write(T.data);
		if(T.left != null) {
			preOrder(T.left);
		}
		if(T.right != null) {
			preOrder(T.right);
		}
		
	}

	static void inOrder(TreeNode T) throws IOException { //중위 (좌 중 우)
		if(T.left != null) {
			inOrder(T.left);
		}
		
		bw.write(T.data);
		
		if(T.right != null) {
			inOrder(T.right);
		}
	}

	static void postOrder(TreeNode T) throws IOException { //후위 (좌 우 중)
		if(T.left != null) {
			postOrder(T.left);
		}
		
		if(T.right != null) {
			postOrder(T.right);
		}
		
		bw.write(T.data);
	}

}
