/**
* Filename : StringOfFind.java
* Author : DengPengFei
* Creation time : ����7:00:04 - 2020��5��10��
*/
package JavaString;

/*
 *  �ַ����Ĳ���  String ��� indexOf() ������ lastlndexOf() �����������ַ����л�ȡƥ���ַ�������������ֵ��
 */

public class StringOfFind {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}
	
	// indexOf() ������ ���ڷ����ַ���������ָ���ַ������״γ��ֵ�����λ�ã�������ҵ����򷵻�����ֵ�����򷵻� -1
	public static void demo1() {
		
		String s = "Hello Java";
		int size = s.indexOf('v');    // size�Ľ��Ϊ8
		
		System.out.println("'v'������Ϊ��"+size);
		
		String words = "today,monday,sunday";
	    System.out.println("ԭʼ�ַ�����'"+words+"'");
	    System.out.println("indexOf(\"day\")�����"+words.indexOf("day"));
	    System.out.println("indexOf(\"day\",5)�����"+words.indexOf("day",5));
	    System.out.println("indexOf(\"o\")�����"+words.indexOf("o"));
	    System.out.println("indexOf(\"o\",6)�����"+words.indexOf("o",6));
		
	}
	
	//  lastlndexOf() ����: ���ڷ����ַ���������ָ���ַ��������һ�γ��ֵ�����λ�ã�������ҵ��򷵻�����ֵ�����򷵻� -1
	public static void demo2() {
		
		// lastIndexOf() �����Ĳ��Ҳ����Ǵ���������ң������ָ����ʼ��������Ĭ�ϴ��ַ�����ĩβ��ʼ���ҡ�
		String words="today,monday,Sunday";
	    System.out.println("ԭʼ�ַ�����'"+words+"'");
	    System.out.println("lastIndexOf(\"day\")�����"+words.lastIndexOf("day"));
	    System.out.println("lastIndexOf(\"day\",5)�����"+words.lastIndexOf("day",5));
	    System.out.println("lastIndexOf(\"o\")�����"+words.lastIndexOf("o"));
	    System.out.println("lastlndexOf(\"o\",6)�����"+words.lastIndexOf("o",6));
		
	}
	
	// charAt() �����������ַ����ڸ���ָ�������������ַ�
	public static void demo3() {
		
		String words = "today,monday,sunday";
		System.out.println(words.charAt(0));    // �����t
		System.out.println(words.charAt(1));    // �����o
		System.out.println(words.charAt(8));    // �����n
		
	}

}
