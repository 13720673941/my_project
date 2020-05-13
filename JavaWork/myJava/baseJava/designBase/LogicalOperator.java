/**
* Filename : LogicalOperator.java
* Author : DengPengFei
* Creation time : 下午4:10:40 - 2020年4月28日
*/

package designBase;

// Java逻辑运算符（&&、||和!）

public class LogicalOperator {
	
	// 逻辑运算符
	public static void testOne() {
		
		
		/*
		 * Java中&&和&的区别: &&的短路功能，当第一个表达式的值为false的时候，则不再计算第二个表达式；&则两个表达式都执行
		 */
		
		
		// && / & 短路与 ab 全为 true 时，计算结果为 true，否则为 false
		System.out.println("逻辑运算符：'&&' "+(3>1&&3<4));
		
		// || / | 短路或	ab 全为 false 时，计算结果为 false，否则为 true
		System.out.println("逻辑运算符：'||' "+(2<1||3<4));
		
		// ! 逻辑非	a 为 true 时，值为 false，a 为 false 时，值为 true
		System.out.println("逻辑运算符：'!' "+(!(2>4)));
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		testOne();
		
	}

}
