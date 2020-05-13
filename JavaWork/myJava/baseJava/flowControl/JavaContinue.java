/**
* Filename : JavaContinue.java
* Author : DengPengFei
* Creation time : ����11:53:42 - 2020��5��6��
*/
package flowControl;

/**
 *   continue��break �������
 *   
 *   break: ��ѭ��ִ�е�break���ʱ,���˳�����ѭ��,Ȼ��ִ��ѭ��������
 *   continue: ��ѭ�����ִ�е�continueʱ,����ѭ������,���¿�ʼ��һ��ѭ��
 */

public class JavaContinue {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//test1();
		test2();
		
	}
	
	// continue �е�ż�� �����������
	public static void test1() {
		
		for (int i = 0; i < 10; i++) {
			
			if (i < 5) {
				
				continue;
				
			}
			System.out.println(i);
			
		}
		
	}
	
	// continue goto ����ʽ
	public static void test2() {
		
		 label1: for (int i = 1; i < 5; i++) {
			for (int j = 1; j < 5; j++) {
				if (i == j) {
					// ���� i==y ������
					continue  label1;
				}
				System.out.println(i+","+j);
			}
		}
		
	}

}
