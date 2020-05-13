/**
* Filename : StringChangeInt.java
* Author : DengPengFei
* Creation time : 下午2:48:40 - 2020年5月9日
*/
package JavaString;

/*
 *   字符串 和 整型 之间的转化
 */

public class StringChangeInt {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}
	
	// String转换为int
	public static void demo1() {
		
		/*
		 *  String 字符串转整型 int 有以下两种方式：
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
	
	// int转换为String
	public static void demo2() {
		
		/*
		 * 整型 int 转 String 字符串类型有以下 3 种方法：
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
