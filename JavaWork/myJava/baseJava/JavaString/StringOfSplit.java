/**
* Filename : StringOfSplit.java
* Author : DengPengFei
* Creation time : ����5:02:28 - 2020��5��9��
*/
package JavaString;

/*
 *   Java�ָ��ַ�����spilt()��
 */

public class StringOfSplit {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}
	
	public static void demo1() {
		
		/*
		 * ʹ�÷ָ���ע�����£�
		
		 * 1����.���͡�|������ת���ַ�������üӡ�\\����
		 * ����á�.����Ϊ�ָ��Ļ�������д��String.split("\\.")������������ȷ�ķָ�����������String.split(".")��
		 * ����á�|����Ϊ�ָ��Ļ�������д��String.split("\\|")������������ȷ�ķָ�����������String.split("|")��
		
		 * 2�������һ���ַ������ж���ָ����������á�|����Ϊ���ַ������磺��acount=? and uu =? or n=?����
		 * ���������ָ�������������String.split("and|or")
		 * 
		 */
		
		String Colors = "Red,Black,White,Yellow,Blue";
		
		// �����Ʒָ����
		String[] arr1 = Colors.split(",");
		
		System.out.println("�ָ�ȫ���ַ�����");
		for (String arr : arr1) {
			System.out.println(arr);
		}
		
		// ���Ʒָ�Ϊ����
		String[] arr2 = Colors.split(",",3);
		
		System.out.println("�ָ�3���ַ�����");
		for (String arr : arr2) {
			System.out.println(arr);
		}
		
	}
	
	public static void demo2() {
		
		String str = "Red and Black or White,Yellow | Blue . red";
		
		// ����ָ����������á�|����Ϊ���ַ� 
		String[] arr1 = str.split(" and | or ");
		System.out.println("����ָ����������á�|����Ϊ���ַ�: ");
		for (String arr : arr1) {
			System.out.println(arr);
		}
		
		// ��.���͡�|������ת���ַ�������üӡ�\\��
		String[] arr2 = str.split(" \\| ");
		System.out.println("��.���͡�|������ת���ַ�������üӡ�\\\\��: ");
		for (String arr : arr2) {
			System.out.println(arr);
		
		}

	}

}
