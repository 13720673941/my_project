/**
* Filename : StringOfSplit.java
* Author : DengPengFei
* Creation time : 下午5:02:28 - 2020年5月9日
*/
package JavaString;

/*
 *   Java分割字符串（spilt()）
 */

public class StringOfSplit {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}
	
	public static void demo1() {
		
		/*
		 * 使用分隔符注意如下：
		
		 * 1）“.”和“|”都是转义字符，必须得加“\\”。
		 * 如果用“.”作为分隔的话，必须写成String.split("\\.")，这样才能正确的分隔开，不能用String.split(".")。
		 * 如果用“|”作为分隔的话，必须写成String.split("\\|")，这样才能正确的分隔开，不能用String.split("|")。
		
		 * 2）如果在一个字符串中有多个分隔符，可以用“|”作为连字符，比如：“acount=? and uu =? or n=?”，
		 * 把三个都分隔出来，可以用String.split("and|or")
		 * 
		 */
		
		String Colors = "Red,Black,White,Yellow,Blue";
		
		// 不限制分割个数
		String[] arr1 = Colors.split(",");
		
		System.out.println("分割全部字符串：");
		for (String arr : arr1) {
			System.out.println(arr);
		}
		
		// 限制分割为三个
		String[] arr2 = Colors.split(",",3);
		
		System.out.println("分割3个字符串：");
		for (String arr : arr2) {
			System.out.println(arr);
		}
		
	}
	
	public static void demo2() {
		
		String str = "Red and Black or White,Yellow | Blue . red";
		
		// 多个分隔符，可以用“|”作为连字符 
		String[] arr1 = str.split(" and | or ");
		System.out.println("多个分隔符，可以用“|”作为连字符: ");
		for (String arr : arr1) {
			System.out.println(arr);
		}
		
		// “.”和“|”都是转义字符，必须得加“\\”
		String[] arr2 = str.split(" \\| ");
		System.out.println("“.”和“|”都是转义字符，必须得加“\\\\”: ");
		for (String arr : arr2) {
			System.out.println(arr);
		
		}

	}

}
