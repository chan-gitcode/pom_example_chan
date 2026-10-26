# Phân Tích POM (Page Object Model)

---

## 1. BasePage

### Phương thức

1. Click
2. Set Text
3. Verify Element Visible
4. Verify Element Text
5. Select Dropdown List
6. Upload File
7. Navigate URL

---

## 2. Page Objects

### 2.1. LoginPage

#### Thuộc tính (Locator của các element)

1. Textbox Username
2. Textbox Password
3. Button Login

#### Phương thức

1. Truy cập URL
2. Đăng nhập với thông tin tài khoản
3. Kiểm tra đăng nhập thành công

---

### 2.2. HomePage

#### Thuộc tính (Locator của các element)

1. Menu Core HR
2. Sub-menu Department

#### Phương thức

1. Kiểm tra hiển thị của Left Menu
2. Click Menu

---

### 2.3. DepartmentPage

#### Thuộc tính (Locator của các element)

1. Textbox Name
2. Button Save
3. Textbox Search
4. "Department Name" Cell Table

#### Phương thức

1. Tạo Department
2. Kiểm tra Department đã tạo

---

### 2.4. DesignationPage

#### Thuộc tính (Locator của các element)

1. Dropdown Department
2. Textbox Designation Name
3. Textbox Description
4. Button Save
5. "Department" Cell Table
6. "Designation" Cell Table
7. Textbox Search

#### Phương thức

1. Tạo Designation
2. Kiểm tra Designation đã tạo

---

### 2.5. PoliciesPage

#### Thuộc tính (Locator của các element)

1. Textbox Title
2. Textbox Description

#### Phương thức

1. Tạo Policies
2. Kiểm tra Policies đã tạo