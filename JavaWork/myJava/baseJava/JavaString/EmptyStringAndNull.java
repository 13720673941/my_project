/**
* Filename : EmptyStringAndNull.java
* Author : DengPengFei
* Creation time : ����6:52:19 - 2020��5��10��
*/
package JavaString;

/*
 *  Java ���ַ��� �� null
 */

public class EmptyStringAndNull {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String str1 = new String();
	    String str2 = null;
	    String str3 = "";
	    System.out.println(str3.length()); // ���ַ���""�ĳ���Ϊ0
	    System.out.println(str2.length()); // �׳���ָ���쳣
	    System.out.println(str1); // ���""
	    System.out.println(str1 == str2); // �ڴ��ַ�ıȽϣ�����false
	    System.out.println(str1.equals(str2)); // ֵ�ıȽϣ�����false
	    System.out.println(str2 == str3); // �ڴ��ַ�ıȽϣ�����false
	    System.out.println(str3.equals(str2)); // ֵ�ıȽϣ�����false
	    System.out.println(str1 == str3); // �ڴ��ַ�ıȽϣ�����false
	    System.out.println(str1.equals(str3)); // ֵ�ıȽϣ�����true
	    
	    // Ҫ���һ���ַ����Ȳ��� null Ҳ��Ϊ�մ�
	    
	    // if (str != null && str.length() != 0)
		
	}

}
