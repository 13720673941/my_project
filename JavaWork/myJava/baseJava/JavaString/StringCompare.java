/**
* Filename : StringCompare.java
* Author : DengPengFei
* Creation time : 下午4:49:32 - 2020年5月10日
*/
package JavaString;

import java.util.Scanner;

/*
 *   Java 中字符串的比较  equals ...
 *   
 *   在 Java 中，比较字符串的常用方法有 3 个：equals() 方法、equalsIgnoreCase() 方法、 compareTo() 方法
 */

public class StringCompare {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo3();
		demo1();
		demo2();
		
	}
	
	// equals() 方法: 逐个地比较两个字符串的每个字符是否相同。如果两个字符串具有相同的字符和长度,对于字符的大小写，也在检查的范围之内
	public static void demo1() {
		
		/*
		 *  在第一次进入系统时要求管理员设置一个密码，出于安全考虑密码需要输入两次，如果两次输入的密码一致才生效，否则提示失败
		 */
		
		System.out.println("欢迎进入《学生信息管理》系统");
		Scanner input = new Scanner(System.in);
		System.out.println("请输入密码：");
		// 获取输入密码字段
		String loginPassword = input.next();
		System.out.println("请确认输入密码：");
		// 获取输入第二次字段
		String confirmPassword = input.next();
		// 判断两次输入密码是否一致
		if (loginPassword.equals(confirmPassword)) {
			System.out.println("密码设置成功！");
		}else {
			System.out.println("请确认两次密码一致！");
		}
		
	}
	
	// equalsIgnoreCase() 方法: 和语法与 equals() 方法完全相同，唯一不同的是 equalsIgnoreCase() 比较时不区分大小写
	public static void demo2() {
		
		/*
		 * 在会员系统中需要输入用户名和密码进行检验，下面使用 equalsIgnoreCase() 方法实现检验登录时不区分用户名和密码的大小写
		 */
		
		System.out.println("欢迎进入《学生信息管理》系统");
		Scanner input = new Scanner(System.in);
		System.out.println("请输入用户名：");
		// 获取输入密码字段
		String username = input.next();
		System.out.println("请输入密码：");
		// 获取输入第二次字段
		String password = input.next();
		// 判断账号密码信息
		if (username.equalsIgnoreCase("admin") && password.equalsIgnoreCase("admincjsh")) {
			System.out.println("登录成功！");
		}else {
			System.out.println("用户名或密码不正确！");
		}
		input.close();
		
	}
	
	// compareTo() 方法: 它会按字典顺序将 str 表示的字符序列与 otherstr 参数表示的字符序列进行比较
	// 如果按字典顺序 str 位于 otherster 参数之前，比较结果为一个负整数；如果 str 位于 otherstr 之后，比较结果为一个正整数；如果两个字符串相等，则结果为 0
	public static void demo3() {
		
		String str = "A";
	    String str1 = "a";
	    System.out.println("str=" + str);
	    System.out.println("str1=" + str1);
	    System.out.println("str.compareTo(str1)的结果是：" + str.compareTo(str1));
	    System.out.println("str1.compareTo(str)的结果是：" + str1.compareTo(str));
	    System.out.println("str1.compareTo('a')的结果是：" + str1.compareTo("a"));
		
	}
	
}
