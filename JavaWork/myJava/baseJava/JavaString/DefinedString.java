/**
* Filename : DefinedString.java
* Author : DengPengFei
* Creation time : 上午9:38:42 - 2020年5月9日
*/
package JavaString;


/*
 *    定义字符串   字符串基础
 */

public class DefinedString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		demo2();
		demo3();

	}
	
	public static void demo1() {
		
		// 字符串的创建
		String str = "我是一只小小鸟"; // 结果：我是一只小小鸟
		String word;
		word = "I am a bird"; // 结果：I am a bird
		word = "<h1>to fly</h1>"; // 结果：<h1>to fly</h1>
		word = "Let\'s say that it\'s true"; // 结果：Let's say that it's true
		System.out.println(word);
		word = "北京\\上海\\广州"; // 结果：北京\上海\广州
		System.out.println(str);
		
	}
	
	// String(char[]value)
	public static void demo2() {
		
		// 分配一个新的字符串，将参数中的字符数组元素全部变为字符串。
		// 该字符数组的内容已被复制，后续对字符数组的修改不会影响新创建的字符串
		char a[] = {'H','e','l','l','o'};
		String sChar = new String(a);
		
		// 修改数组中索引为 1 的值
		a[1] = 's';
		System.out.println(sChar);
		
	}
	
	// String(char[] value,int offset,int count)
	public static void demo3() {
		
		// 分配一个新的 String，它包含来自该字符数组参数一个子数组的字符。
		// offset 参数是子数组第一个字符的索引，count 参数指定子数组的长度。
		// 该子数组的内容已被赋值，后续对字符数组的修改不会影响新创建的字符串
		char a[]={'H','e','l','l','o'};
		String sChar=new String(a,1,4);
		a[1]='s';
		System.out.println(sChar);
	
	}
	
}
