package com.example.userservice.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "users")  // 테이블 이름을 "user"로 지정
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String email;

    // 기본 생성자
    public User() {}

    // 생성자
    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    // Getter와 Setter 추가
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}