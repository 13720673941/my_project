/**
* Filename : LogicalOperator.java
* Author : DengPengFei
* Creation time : ����4:10:40 - 2020��4��28��
*/

package designBase;

// Java�߼��������&&��||��!��

public class LogicalOperator {
	
	// �߼������
	public static void testOne() {
		
		
		/*
		 * Java��&&��&������: &&�Ķ�·���ܣ�����һ�����ʽ��ֵΪfalse��ʱ�����ټ���ڶ������ʽ��&���������ʽ��ִ��
		 */
		
		
		// && / & ��·�� ab ȫΪ true ʱ��������Ϊ true������Ϊ false
		System.out.println("�߼��������'&&' "+(3>1&&3<4));
		
		// || / | ��·��	ab ȫΪ false ʱ��������Ϊ false������Ϊ true
		System.out.println("�߼��������'||' "+(2<1||3<4));
		
		// ! �߼���	a Ϊ true ʱ��ֵΪ false��a Ϊ false ʱ��ֵΪ true
		System.out.println("�߼��������'!' "+(!(2>4)));
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		testOne();
		
	}

}
