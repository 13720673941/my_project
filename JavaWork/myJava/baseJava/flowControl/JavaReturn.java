/**
* Filename : JavaReturn.java
* Author : DengPengFei
* Creation time : ����5:18:19 - 2020��4��30��
*/
package flowControl;

/*
 *   Java �е�return���÷�
 */

public class JavaReturn {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(test1(1,2));

	}
	
	/**
	 * �������� ��������ֵ�ĺ�
	 * 
	 * @param number1
	 * @param number2
	 * @return
	 */
	public static double test1(double number1,double number2) {
		
		double sum = number1 + number2;
		
		return sum;
		
	}

}
