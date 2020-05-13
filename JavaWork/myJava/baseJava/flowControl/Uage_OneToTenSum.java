/**
* Filename : Uage_OneToTenSum.java
* Author : DengPengFei
* Creation time : 下午2:38:21 - 2020年4月30日
*/
package flowControl;

/*
 * 
 * 			分别用 for、do-while 和 while 求出 1-10 的和 
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
		System.out.println("for 循环求1-10的和为："+result);
		
	}
	
	// do - while 
	public static void test2() {
		
		int result = 0,number = 1;
		
		do {
			result += number;
			number ++;
		} while (number <= 10);
		System.out.println("do - while 循环求1-10的和为："+result);
		
	}
	
	// while 
	public static void test3() {
		
		int result = 0,number = 1;
		
		while (number <= 10) {
			result+=number;
			number++;
		}
		System.out.println("while 循环求1-10的和为："+result);
		
	}

}
