/**
* Filename : DefinedString.java
* Author : DengPengFei
* Creation time : ����9:38:42 - 2020��5��9��
*/
package JavaString;


/*
 *    �����ַ���   �ַ�������
 */

public class DefinedString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		demo2();
		demo3();

	}
	
	public static void demo1() {
		
		// �ַ����Ĵ���
		String str = "����һֻСС��"; // ���������һֻСС��
		String word;
		word = "I am a bird"; // �����I am a bird
		word = "<h1>to fly</h1>"; // �����<h1>to fly</h1>
		word = "Let\'s say that it\'s true"; // �����Let's say that it's true
		System.out.println(word);
		word = "����\\�Ϻ�\\����"; // ���������\�Ϻ�\����
		System.out.println(str);
		
	}
	
	// String(char[]value)
	public static void demo2() {
		
		// ����һ���µ��ַ������������е��ַ�����Ԫ��ȫ����Ϊ�ַ�����
		// ���ַ�����������ѱ����ƣ��������ַ�������޸Ĳ���Ӱ���´������ַ���
		char a[] = {'H','e','l','l','o'};
		String sChar = new String(a);
		
		// �޸�����������Ϊ 1 ��ֵ
		a[1] = 's';
		System.out.println(sChar);
		
	}
	
	// String(char[] value,int offset,int count)
	public static void demo3() {
		
		// ����һ���µ� String�����������Ը��ַ��������һ����������ַ���
		// offset �������������һ���ַ���������count ����ָ��������ĳ��ȡ�
		// ��������������ѱ���ֵ���������ַ�������޸Ĳ���Ӱ���´������ַ���
		char a[]={'H','e','l','l','o'};
		String sChar=new String(a,1,4);
		a[1]='s';
		System.out.println(sChar);
	
	}
	
}
