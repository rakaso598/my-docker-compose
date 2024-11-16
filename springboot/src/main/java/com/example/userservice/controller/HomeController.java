package com.example.userservice.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    @GetMapping("/")
    public String home(Model model) {
        // 데이터를 모델에 추가 (옵션)
        model.addAttribute("message", "Welcome to the User Management Service!");
        return "index";
    }
}