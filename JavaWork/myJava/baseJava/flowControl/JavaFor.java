/**
* Filename : JavaFor.java
* Author : DengPengFei
* Creation time : ����12:02:55 - 2020��4��30��
*/
package flowControl;

/*
 * 		for(�������ʽ1;�������ʽ2;�������ʽ3) {
 *   		����;
 *		}
 *
 *	�������ʽ1��ѭ���ṹ�ĳ�ʼ���֣�Ϊѭ����������ֵ  int i=1
 *	�������ʽ2��ѭ���ṹ��ѭ������ i>40
 *	�������ʽ3��ѭ���ṹ�ĵ������֣�ͨ�������޸�ѭ��������ֵ i++
 *
 *	for �ؼ��ֺ��������е� 3 ���������ʽ�����á�;������
 */

public class JavaFor {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
		test2();
		test3();
		test4();
		
	}
	
	// for - each 
	public static void test1() {
		
		int c[] = {1,2,3,4,5};
		
		for (int i:c) {
			
			if (i == 2 || i == 4) {
				
				i = i * 10;
				
			}
			System.out.println(i); 
		}
		
	}
	
	// for ѭ�����
	public static void test2() {
		
		// ��ʼ��ֵ
		int result = 1;
		// ѭ���ṹ
		for (int number = 1; number < 11; number++) {
			
			System.out.println("for ѭ����"+(result+=number));
			
		}
		
	}
	
	// for ����г�ʼ����ѭ�������Լ��������ֶ�����Ϊ����䣨���ֺŲ���ʡ�ԣ������߾�Ϊ�յ�ʱ���൱��һ������ѭ��
	public static void test3() {
		
		// ʹ�� for ����������ʽ���� 1~100 ���������ĺ͡�
		int result = 0;
		int number = 1;
		
		for (; number < 101; number++) {
			
			// �ж��Ƿ�Ϊ����
			if (number%2 != 0) {
				
				result += number;
				
			}
		}
		System.out.println("100���ڵ������ܺ�Ϊ��"+result);
		
	}
	
	public static void test4() {
		
		int result = 0;
		int number = 1;
		
		// for ѭ������������������Ϊ�� ���� �� ; ���ֺű����� �������Էŵ�ѭ������
		for (;;) {
			
			if (number > 100) {
				break;
			}
			if (number%2==0) {
				result+=number;
			}
			number++;
		}
		System.out.println("100���ڵ�ż���ܺ�Ϊ��"+result);
		
	}

}
