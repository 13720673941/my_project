/**
* Filename : JavaReturn.java
* Author : DengPengFei
* Creation time : 下午5:18:19 - 2020年4月30日
*/
package flowControl;

/*
 *   Java 中的return的用法
 */

public class JavaReturn {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(test1(1,2));

	}
	
	/**
	 * 创建方法 计算两个值的和
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
