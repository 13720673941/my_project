/**
* Filename : StringChangeInt.java
* Author : DengPengFei
* Creation time : ����2:48:40 - 2020��5��9��
*/
package JavaString;

/*
 *   �ַ��� �� ���� ֮���ת��
 */

public class StringChangeInt {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}
	
	// Stringת��Ϊint
	public static void demo1() {
		
		/*
		 *  String �ַ���ת���� int ���������ַ�ʽ��
		 *  Integer.parseInt(str)
		 *  Integer.valueOf(str).intValue()
		 */
		
		String str1 = "100";
		
		int number = 0;
		
		number = Integer.parseInt(str1);
		System.out.println(1+number);
		
		number = Integer.valueOf(str1).intValue();
		System.out.println(1+number);
		
	}
	
	// intת��ΪString
	public static void demo2() {
		
		/*
		 * ���� int ת String �ַ������������� 3 �ַ�����
		 * String s = String.valueOf(i);
		 * String s = Integer.toString(i);
		 * String s = "" + i;
		 */
		
		int number = 100;
		
		// 
		String str1 = String.valueOf(number);
		System.out.println("str1: "+str1);
		
		// 
		String str2 = Integer.toString(number);
		System.out.println("str2: "+str2);
		
		//
		String str3 = number + "";
		System.out.println("str3: "+str3);
		
	}

}
