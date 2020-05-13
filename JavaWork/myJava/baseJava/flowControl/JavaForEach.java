/**
* Filename : JavaForEach.java
* Author : DengPengFei
* Creation time : ����4:53:45 - 2020��4��30��
*/
package flowControl;

public class JavaForEach {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
		test2();
		
	}
	
	// ������һ�����飬���� for ����������ķ�ʽ����
	public static void test1() {
		
		int number[] = {1,2,3,4,5,6};
		
		for (int i = 0; i < number.length; i++) {
			System.out.println(number[i]);
		}
		
		System.out.println("------- for each -------");
		
		for (int i : number) {
			System.out.println(i);
		}
		
	}
	
	// ��һ���ַ��������д洢�˼��ֱ�����ԣ����ڽ���Щ������Ա��������
	public static void test2() {
		
		String [] languageStrings = {"python","java","php","js"};
		
		for (String language : languageStrings) {
			System.out.println(language);
		}
		
	}

}
