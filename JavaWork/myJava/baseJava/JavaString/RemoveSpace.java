/**
* Filename : RemoveSpace.java
* Author : DengPengFei
* Creation time : ����3:55:08 - 2020��5��9��
*/
package JavaString;

/*
 *  ȥ���ַ����еĿո�     
 *  
 *  str.replace(" ", "");   ȥ���ַ����м�ո�
 *  str.trim();				ȥ��ǰ��ո�
 */

public class RemoveSpace {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}
	
	// �ַ�����.trim()
	public static void demo1() {
		
		/*
		 * trim() ֻ��ȥ���ַ�����ǰ��İ�ǿո�Ӣ�Ŀո񣩣����޷�ȥ��ȫ�ǿո����Ŀո񣩡�
		 * �������´��뽫ȫ�ǿո��滻Ϊ��ǿո��ٽ��в����������滻�� String ��� replace() ����
		 */
		
		String str1 = " Hello ";
		System.out.println(str1.length());
		
		String str2 = str1.trim();
		System.out.println(str2.length());
		
	}
	
	// �����ַ����ո�ȥ��  
	public static void demo2() {
		
		String str1 = " ����  �� ";
		
		// �����Ŀո��滻ΪӢ�Ŀո�
		String str = str1.replace((char)12288,' ');
		str = str.trim();
		System.out.println("ȥ��ǰ��ո�������ַ�����"+str);
		
		// ȥ���м�Ŀո�
		str = str.replace(" ", "");
		System.out.println("ȥ���м�ո�������ַ�����"+str);
		
	}

}

