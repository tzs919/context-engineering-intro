package com.example.demo.controller;

import com.example.demo.dto.UserDTO;
import com.example.demo.service.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.web.servlet.MockMvc;

import java.util.Arrays;
import java.util.List;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

/**
 * Controller 层测试
 * 使用 @WebMvcTest 只加载 Web 层
 * 使用 MockMvc 模拟 HTTP 请求
 */
@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    @WithMockUser
    void shouldReturnAllUsers() throws Exception {
        // 准备测试数据
        List<UserDTO> users = Arrays.asList(
            createUserDTO(1L, "user1", "user1@example.com"),
            createUserDTO(2L, "user2", "user2@example.com")
        );

        when(userService.getAllUsers()).thenReturn(users);

        // 执行测试
        mockMvc.perform(get("/api/users"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].username").value("user1"))
                .andExpect(jsonPath("$[1].username").value("user2"));
    }

    @Test
    @WithMockUser
    void shouldReturnUserById() throws Exception {
        UserDTO user = createUserDTO(1L, "user1", "user1@example.com");

        when(userService.getUserById(1L)).thenReturn(user);

        mockMvc.perform(get("/api/users/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.username").value("user1"));
    }

    @Test
    @WithMockUser
    void shouldCreateUser() throws Exception {
        UserDTO userDTO = createUserDTO(null, "newuser", "new@example.com");
        UserDTO created = createUserDTO(1L, "newuser", "new@example.com");

        when(userService.createUser(any(UserDTO.class))).thenReturn(created);

        mockMvc.perform(post("/api/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"username\":\"newuser\",\"email\":\"new@example.com\"}"))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.username").value("newuser"));
    }

    private UserDTO createUserDTO(Long id, String username, String email) {
        UserDTO dto = new UserDTO();
        dto.setId(id);
        dto.setUsername(username);
        dto.setEmail(email);
        return dto;
    }
}
