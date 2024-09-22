# tfidf Vector

## Start

```sh
sudo docker compose up -d --build
```

```sh
sudo docker compose logs
```

```sh
sudo docker ps
```

Link: http://127.0.0.1:8000/docs

## Document

- [vietnamese-stopwords](https://github.com/stopwords/vietnamese-stopwords)

## Test
```sh
{
 "text1": "Tỷ phú Vượng đề xuất về nhà ở xã hội, công nghiệp hỗ trợ. Sáng 21/9, Thủ tướng    Chính phủ Phạm Minh Chính chủ trì Hội nghị Thường trực Chính phủ làm việc với các doanh nghiệp lớn về giải pháp góp phần phát triển kinh tế - xã hội đất nước. Liên quan vấn đề an sinh trọng tâm là nhà ở xã hội, ông Phạm Nhật Vượng - Chủ tịch Vingroup - đề xuất Chính phủ có cơ chế chỉ định nhà đầu tư để rút ngắn thời gian hoàn thành các thủ tục, vì hạn chế lớn nhất hiện nay đối với nhà ở xã hội là liên quan nội dung về 10% lợi nhuận. Cụ thể, ông Vượng phản ánh, nếu các doanh nghiệp bất động sản triển khai hoạt động này với lợi nhuận 10% thì không thể làm được, vì chỉ tồn đọng vốn 1-2 năm hoặc bán chậm 1-2 năm là sẽ lỗ, trong khi nhà ở xã hội mang tính đóng góp, không phải là kinh doanh. Vingroup đề nghị tăng tiêu chuẩn của nhà ở xã hội, tức là phải có hầm để xe, phải có khu vui chơi cho trẻ cũng như các tiện ích khác. Liên quan đến lĩnh vực công nghiệp hỗ trợ, ông đề nghị Chính phủ có các cơ chế để hỗ trợ cho các doanh nghiệp vừa và nhỏ để họ có đủ điều kiện ban đầu tham gia vào chuỗi công nghiệp hỗ trợ. Ông Vượng cho rằng nếu chúng ta đẩy mạnh được vấn đề này, Việt Nam sẽ có nền công nghiệp phụ trợ rất mạnh.",
 "text2": "Cổ phiếu Tân Tạo bị đình chỉ giao dịch. Sở Giao dịch Chứng khoán TPHCM (HoSE) vừa quyết định đình chỉ giao dịch đối với cổ phiếu của Công ty Cổ phần Đầu tư và Công nghiệp Tân Tạo (mã chứng khoán: ITA) kể từ ngày 26/9. Lý do là Tân Tạo vi phạm nhiều lần các quy định về công bố thông tin trên thị trường chứng khoán, mặc dù trước đó đã bị đưa vào diện hạn chế giao dịch. Theo quy định của HoSE, các công ty vi phạm nghiêm trọng sẽ bị đình chỉ giao dịch để bảo vệ quyền lợi của nhà đầu tư. Theo HoSE, Tân Tạo chưa công bố báo cáo tài chính kiểm toán năm 2023, báo cáo thường niên năm 2023 và báo cáo tài chính soát xét bán niên năm 2024. Trước đó, Tân Tạo cũng đã gửi công văn gửi đến Ủy ban Chứng khoán Nhà nước (UBCKNN) và HoSE, đề nghị được tạm hoãn công bố báo cáo tài chính kiểm toán năm 2023 và báo cáo tài chính soát xét bán niên năm 2024 do những khó khăn khách quan. Tuy nhiên, các cơ quan quản lý vẫn chưa chấp thuận yêu cầu này. Phía doanh nghiệp trần tình rằng, mặc dù đã nỗ lực hết sức, liên hệ làm việc và thuyết phục tất cả công ty kiểm toán (30 công ty được chấp thuận kiểm toán cho đơn vị có lợi ích công chúng thuộc lĩnh vực chứng khoán năm 2023), nhưng đều bị từ chối."
}
```

From [dantri](https://dantri.com.vn/)

From [dantri-paper](https://dantri.com.vn/kinh-doanh/dn-tuan-qua-kien-nghi-cua-nhung-nguoi-giau-nhat-nuoc-loat-tin-ve-flc-ita-20240922074706149.htm)

## End

```sh
sudo docker compose down
```
