/**
* Filename : StringOfJoint.java
* Author : DengPengFei
* Creation time : ����3:07:37 - 2020��5��9��
*/
package JavaString;

/*
 *   Java �ַ�����ƴ��
 */

public class StringOfJoint {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		demo3();
		
	}
	
	// ʹ�������������+��
	public static void demo1() {
		
		int number[] = {101,102,103,104,105};
		String names[] = {"�³̰�","����ϼ","�ܹ���","÷����","����ΰ"};
		String classes[] = {"��ѧ","����","Ӣ��","��ѧ","����"};
		// ѭ��������ӡ
		for (int i = 0; i < number.length; i++) {
			System.out.println("ѧ�ţ�"+number[i]+"|������"+names[i]+"|�γ̣�"+classes[i]+"|�༶��������������");
		}
		
	}
	
	// ʹ�� concat() ����
	public static void demo2() {
		
		// �ַ��� 1.concat(�ַ��� 2);
		String name = "������";
		name = name.concat("��");
		name = name.concat("27��");
		System.out.println(name);
		
		String cn = "�й�";
	    System.out.println(cn.concat("����").concat("������").concat("����԰"));
		
	}
	
	// ����������������
	public static void demo3() {
		
		// ʵ�ֽ��ַ��������͡������ͱ���������������
		String name = "DPF"; 
		int age = 27;
		float tall = 175.3f;
		
		System.out.print("�ҵ����ֽУ�"+name+"\n���䣺"+age+"\n��ߣ�"+tall);
		
	}
	
}
