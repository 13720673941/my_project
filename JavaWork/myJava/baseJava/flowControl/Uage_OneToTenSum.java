/**
* Filename : Uage_OneToTenSum.java
* Author : DengPengFei
* Creation time : ����2:38:21 - 2020��4��30��
*/
package flowControl;

/*
 * 
 * 			�ֱ��� for��do-while �� while ��� 1-10 �ĺ� 
 * 
 */

public class Uage_OneToTenSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
		test2();
		test3();
	}
	
	// for 
	public static void test1() {
		
		int result = 0,number = 1;
		
		for (;number <= 10;number++) {
			result+=number;
		}
		System.out.println("for ѭ����1-10�ĺ�Ϊ��"+result);
		
	}
	
	// do - while 
	public static void test2() {
		
		int result = 0,number = 1;
		
		do {
			result += number;
			number ++;
		} while (number <= 10);
		System.out.println("do - while ѭ����1-10�ĺ�Ϊ��"+result);
		
	}
	
	// while 
	public static void test3() {
		
		int result = 0,number = 1;
		
		while (number <= 10) {
			result+=number;
			number++;
		}
		System.out.println("while ѭ����1-10�ĺ�Ϊ��"+result);
		
	}

}
