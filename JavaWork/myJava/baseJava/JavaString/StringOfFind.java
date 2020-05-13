/**
* Filename : StringOfFind.java
* Author : DengPengFei
* Creation time : 下午7:00:04 - 2020年5月10日
*/
package JavaString;

/*
 *  字符串的查找  String 类的 indexOf() 方法和 lastlndexOf() 方法用于在字符串中获取匹配字符（串）的索引值。
 */

public class StringOfFind {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}
	
	// indexOf() 方法： 用于返回字符（串）在指定字符串中首次出现的索引位置，如果能找到，则返回索引值，否则返回 -1
	public static void demo1() {
		
		String s = "Hello Java";
		int size = s.indexOf('v');    // size的结果为8
		
		System.out.println("'v'的索引为："+size);
		
		String words = "today,monday,sunday";
	    System.out.println("原始字符串是'"+words+"'");
	    System.out.println("indexOf(\"day\")结果："+words.indexOf("day"));
	    System.out.println("indexOf(\"day\",5)结果："+words.indexOf("day",5));
	    System.out.println("indexOf(\"o\")结果："+words.indexOf("o"));
	    System.out.println("indexOf(\"o\",6)结果："+words.indexOf("o",6));
		
	}
	
	//  lastlndexOf() 方法: 用于返回字符（串）在指定字符串中最后一次出现的索引位置，如果能找到则返回索引值，否则返回 -1
	public static void demo2() {
		
		// lastIndexOf() 方法的查找策略是从右往左查找，如果不指定起始索引，则默认从字符串的末尾开始查找。
		String words="today,monday,Sunday";
	    System.out.println("原始字符串是'"+words+"'");
	    System.out.println("lastIndexOf(\"day\")结果："+words.lastIndexOf("day"));
	    System.out.println("lastIndexOf(\"day\",5)结果："+words.lastIndexOf("day",5));
	    System.out.println("lastIndexOf(\"o\")结果："+words.lastIndexOf("o"));
	    System.out.println("lastlndexOf(\"o\",6)结果："+words.lastIndexOf("o",6));
		
	}
	
	// charAt() 方法可以在字符串内根据指定的索引查找字符
	public static void demo3() {
		
		String words = "today,monday,sunday";
		System.out.println(words.charAt(0));    // 结果：t
		System.out.println(words.charAt(1));    // 结果：o
		System.out.println(words.charAt(8));    // 结果：n
		
	}

}
