// Simple Java OOP example

class Student {

    // Properties
    String name;
    int age;

    // Constructor
    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method
    void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class OOPDemo {

    public static void main(String[] args) {

        // Create an object
        Student student = new Student("Siddartha", 21);

        // Call the method
        student.displayInfo();
    }
}
