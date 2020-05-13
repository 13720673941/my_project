/**
* Filename : JavaFor.java
* Author : DengPengFei
* Creation time : 下午12:02:55 - 2020年4月30日
*/
package flowControl;

/*
 * 		for(条件表达式1;条件表达式2;条件表达式3) {
 *   		语句块;
 *		}
 *
 *	条件表达式1：循环结构的初始部分，为循环变量赋初值  int i=1
 *	条件表达式2：循环结构的循环条件 i>40
 *	条件表达式3：循环结构的迭代部分，通常用来修改循环变量的值 i++
 *
 *	for 关键字后面括号中的 3 个条件表达式必须用“;”隔开
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
	
	// for 循环语句
	public static void test2() {
		
		// 初始化值
		int result = 1;
		// 循环结构
		for (int number = 1; number < 11; number++) {
			
			System.out.println("for 循环："+(result+=number));
			
		}
		
	}
	
	// for 语句中初始化、循环条件以及迭代部分都可以为空语句（但分号不能省略），三者均为空的时候，相当于一个无限循环
	public static void test3() {
		
		// 使用 for 语句的这种形式计算 1~100 所有奇数的和。
		int result = 0;
		int number = 1;
		
		for (; number < 101; number++) {
			
			// 判断是否为奇数
			if (number%2 != 0) {
				
				result += number;
				
			}
		}
		System.out.println("100以内的奇数总和为："+result);
		
	}
	
	public static void test4() {
		
		int result = 0;
		int number = 1;
		
		// for 循环中三个条件都可以为空 但是 “ ; ”分号必须有 条件可以放到循环下面
		for (;;) {
			
			if (number > 100) {
				break;
			}
			if (number%2==0) {
				result+=number;
			}
			number++;
		}
		System.out.println("100以内的偶数总和为："+result);
		
	}

}
