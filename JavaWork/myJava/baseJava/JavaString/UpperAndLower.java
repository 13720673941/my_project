/**
* Filename : UpperAndLower.java
* Author : DengPengFei
* Creation time : ����3:49:34 - 2020��5��9��
*/
package JavaString;

/*
 *   �ַ����Ĵ�Сдת��
 */

public class UpperAndLower {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		
	}
	
	public static void demo1() {
		
		/*
		 *  �ַ�����.toLowerCase()   ���ַ����е���ĸȫ��ת��ΪСд������ĸ����Ӱ��
		 *  �ַ�����.toUpperCase()   ���ַ����е���ĸȫ��ת��Ϊ��д������ĸ����Ӱ��
		 */
		
		String str1 = "asdasdasasd";
		String str2 = "ASDASDASDAS";
		
		System.out.println(str1.toUpperCase());
		System.out.println(str2.toLowerCase());
		
	}

}
