/**
* Filename : StringOfReplace.java
* Author : DengPengFei
* Creation time : ����5:45:54 - 2020��5��9��
*/
package JavaString;

/*
 *   Java �ַ������滻 replace()
 *   
 *   String ���ṩ�� 3 ���ַ����滻�������ֱ��� replace()��replaceFirst() �� replaceAll()
 */

public class StringOfReplace {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		demo3();
		demo4();
		
	}
	
	// replace()
	public static void demo1() {
		
		String str1 = "hello world";
		
		System.out.println(str1.replace("world", "������"));
		
	}
	
	// replaceFirst()
	public static void demo2() {
		
		String str1 = "hello world";
		
		// �滻�ַ����е�һ�� o 
		System.out.println(str1.replaceFirst("o", "aaa"));
		
	}
	
	// replaceAll()
	public static void demo3() {
		
		String str1 = "hello world";
		
		// �滻�ַ�����ȫ���� o
		System.out.println(str1.replaceAll("o", "bbb"));
		
	}
	
	// Java�ַ����滻ʵ��
	public static void demo4() {
		
		/*
		 * ������һ���ı������кܶ���������֡�����ʹ�� Java �е��ַ����滻�����������������޸ĺ;�����
		 * ���о��õ��������ڡ�Java�ַ������滻��һ����ѧ���� String ��� replace() ������replaceFirst() ������ replaceAll() ����
		 */
		
		// ����ԭʼ�ַ���
	    String intro = "����ʱ�����죬����ʱ�����졣����ȥ����ˣ�©���ڼ�д��ҵ��" + "������ҵʱ���䡱д 5 �У���ѧʹ�� 10 ҳ��";
	    
	    // ���ı��е�����"ʱ"��"ʹ"���滻Ϊ"��"
	    String newStrFirst = intro.replaceAll("[ʱʹ]", "��");
	    // ���ı��е�����"����"��Ϊ"����"
	    String newStrSecond = newStrFirst.replaceAll("����", "����");
	    // ���ı��е�����"©��"��Ϊ"����"
	    String newStrThird = newStrSecond.replaceAll("©��", "����");
	    // ���ı��е�һ�γ��ֵ�"��"��Ϊ"��"
	    String newStrFourth = newStrThird.replaceFirst("[��]", "��");
	    // ��������ַ���
	    System.out.println(newStrFourth);
		
	}

}
