/**
* Filename : JavaWhile.java
* Author : DengPengFei
* Creation time : 上午9:33:12 - 2020年4月30日
*/
package flowControl;

/*
 *   Java 中的while语句 do-while 循环语句的特点是先执行循环体，然后判断循环条件是否成立
 *   
 *   while 循环和 do-while 循环的不同处如下：
 *   语法不同：与 while 循环相比，do-while 循环将 while 关键字和循环条件放在后面，而且前面多了 do 关键字，后面多了一个分号
 *   执行次序不同：while 循环先判断，再执行。do-while 循环先执行，再判断。
 *   一开始循环条件就不满足的情况下，while 循环一次都不会执行，do-while 循环则不管什么情况下都至少执行一次。
 */

public class JavaWhile {
	
	// while 循环语句
	public static void test1() {
		
		int number = 1;
		
		while (number < 10) {
			
			System.out.println("哈哈哈！");
			
			number ++;
			
		}
		
	}

	// do - while 循环语句
	public static void test2() {
		
		int number = 1,result = 1;
	    do {
	        result*=number;
	        number++;
	    }while(number <= 10);
	    
	    System.out.print("10阶乘结果是："+result+"\n");
		
	}
	
	// 在一个图书系统的推荐图书列表中保存了 50 条信息，现在需要让它每行显示 10 条，分 5 行进行显示。下面使用 do-while 循环语句来实现这个效果
	public static void test3() {
		
		int bookIndex = 1;
		
		do {
			
			// print 标准输出 不换行 
			System.out.print(bookIndex+"\t");
			
			if (bookIndex%10==0) {
				System.out.println();
			}
			
			bookIndex++;
			
		} while (bookIndex < 101);
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		test1();
		test2();
		test3();

	}

}
