/**
* Filename : UpperAndLower.java
* Author : DengPengFei
* Creation time : 下午3:49:34 - 2020年5月9日
*/
package JavaString;

/*
 *   字符串的大小写转化
 */

public class UpperAndLower {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		
	}
	
	public static void demo1() {
		
		/*
		 *  字符串名.toLowerCase()   将字符串中的字母全部转换为小写，非字母不受影响
		 *  字符串名.toUpperCase()   将字符串中的字母全部转换为大写，非字母不受影响
		 */
		
		String str1 = "asdasdasasd";
		String str2 = "ASDASDASDAS";
		
		System.out.println(str1.toUpperCase());
		System.out.println(str2.toLowerCase());
		
	}

}
