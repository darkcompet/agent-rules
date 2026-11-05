# Quy chuẩn viết spec

Spec là contract của project; mỗi file có một scope contract độc lập, không phải
một feature hay một task. Một spec có thể chứa nhiều feature liên quan. Code,
test và runbook phải implement và verify các yêu cầu `Approved`, vì chúng là
behavior đã được owner duyệt. Khi code và spec mâu thuẫn, spec thắng; implementation
không tự thay đổi contract.

`Features` là nơi duy nhất định nghĩa feature để tránh các bản contract mâu thuẫn.
Mỗi feature có ID, trạng thái, các bước ngắn bằng ngôn ngữ nghiệp vụ, chi tiết cần
thiết và cách kiểm chứng. Không tạo thêm phần `Chi tiết feature` để chép lại nội dung.

Người đọc phải nắm được mục tiêu và các luồng chính trong 30 giây bằng cách đọc
`Overview` và tiêu đề/các bước đầu của từng feature. Phần còn lại trong feature
giữ đầy đủ contract để implement và review; cách chia này giúp định hướng nhanh
mà không lược bỏ điều kiện cần để thực hiện đúng.

**Cách dùng:** copy `Mẫu` bên dưới vào `docs/specs/<domain>/<scope-slug>.md` → điền theo `Cách điền` → thay nội dung minh họa theo scope → chạy `Tự kiểm`.

## Chọn file spec

- Spec là file theo **scope contract**, không phải file theo feature hoặc task. Một file chứa một outcome contract độc lập và có thể định nghĩa nhiều feature liên quan trong `Features`.
- Trước khi tạo file, tìm trong `catalog.md` và các spec hiện có. Nếu thay đổi
  thuộc cùng outcome/workflow hoặc phải giữ chung invariant/state, cập nhật spec
  hiện có; thêm hoặc sửa feature và requirement trong file đó. Tái sử dụng đúng
  scope giúp giữ một nguồn contract và tránh yêu cầu trùng hoặc mâu thuẫn.
- Tạo spec riêng khi outcome có mục tiêu và acceptance criteria riêng, có thể được review, duyệt, implement và verify độc lập, đồng thời không cần thay đổi contract của spec khác.
- Không tạo file mới chỉ vì task mới, feature mới, requirement mới, component khác hoặc implementation nằm ở PR khác. Nếu ranh giới contract không rõ và lựa chọn ảnh hưởng behavior hay acceptance criteria, hỏi task owner.
- Domain folder chỉ giúp tìm file; hai spec trong cùng folder vẫn có thể có scope độc lập, và một spec không được chia chỉ để làm folder cân bằng.

## Mẫu

Nội dung dưới đây chỉ minh họa một task có behavior. Dùng cùng khung cho task khác; thêm/bỏ detail theo loại task.

````md
# <Tên spec>
Status: Draft · Audited: Not yet

## Overview
<Mục tiêu của task trong một câu.>

## Scope
<Quy định gì. Không quy định gì.>

## Features

### INC-001. Phát hiện input thay đổi
**Loại:** `behavior` · **Thẻ:** `read-only` · **Trạng thái:** Proposed · Todo

1. Khi `gen` chạy, hệ thống phải so hash từng input với `.gen/cache.json`.
2. Nếu hash khớp, hệ thống phải bỏ qua input.
3. Nếu hash khác hoặc chưa có, hệ thống phải đánh dấu input để tạo lại.

**Kiểm chứng**
- INC-001-C1: Input không đổi, chạy `gen` → output không bị ghi hoặc xóa. `Verified: -`
- INC-001-C2: Input thay đổi, chạy `gen` → input đó được đánh dấu để tạo lại. `Verified: -`

### INC-002. Tạo lại input thay đổi và cập nhật cache
**Loại:** `behavior` · **Thẻ:** `ext-write` · **Trạng thái:** Proposed · Todo

1. Hệ thống phải tạo lại các input được đánh dấu thay đổi.
2. Sau khi tạo xong, hệ thống phải lưu hash mới vào `.gen/cache.json`.
3. Khi chạy lại với input không đổi, hệ thống không được tạo trùng output.
4. Nếu lần chạy trước timeout, hệ thống phải đối soát output trước khi retry.

**Kiểm chứng**
- INC-002-C1: Input thay đổi, chạy `gen` → output được cập nhật và hash được lưu. `Verified: -`
- INC-002-C2: Chạy lại với input không đổi → output không được ghi trùng. `Verified: -`
- INC-002-C3: Retry sau timeout → output không bị ghi trùng. `Verified: -`

## Proposed changes
| Target ID | Loại (Change/Remove) | Hiện tại | Đề xuất | Ảnh hưởng |
|---|---|---|---|---|

## Open questions
- [Gating] ...

````

## Cách điền

**Overview, `Scope` và `Features`**
- `Overview` nêu kết quả chung mà spec định nghĩa, trong một câu; không đưa chi tiết thiết kế vào đây.
- `Scope` nêu ranh giới của spec, tối đa 2 câu. Scope là đơn vị contract được review/duyệt; một scope có thể chứa nhiều feature cùng outcome, workflow hoặc lifecycle.
- `Features` là nơi duy nhất định nghĩa feature, không phải bảng mục lục. Mỗi feature có đúng một requirement ID; đặt ID đầu heading theo dạng `### <ID>. <Tên outcome>`.
- Giữ `Overview` và `Scope` riêng, theo thứ tự `Overview` → `Scope` → `Features`. `Overview` tóm tắt outcome; `Scope` xác định ranh giới contract.
- Khi spec mô tả dataflow hoặc workflow qua ít nhất hai service/system hoặc qua nhiều trust boundary, `Overview` phải có Mermaid diagram tổng quan. Diagram phải thể hiện các actor/service tham gia, hướng luồng data/control và ID của các feature liên quan. Ghi rõ trust boundary, secret/plaintext/ciphertext hoặc dữ liệu chỉ tồn tại trong memory khi các phân biệt đó cần để hiểu luồng.
- Diagram tổng quan phải bao quát các feature cùng tham gia luồng xuyên boundary; không ép feature độc lập như `nfr`, `deliverable` hoặc `config` vào runtime flow. Dùng `flowchart` cho dataflow/quan hệ hệ thống; dùng `sequenceDiagram` trong feature liên quan khi thứ tự tương tác giữa service cần làm rõ.
- Sơ đồ chỉ giúp người đọc hiểu quan hệ và trỏ tới feature ID; mọi requirement vẫn phải được định nghĩa trong `Features`. Không thêm contract chỉ có trong sơ đồ, không chép lại toàn bộ bước/điều kiện từ feature vào sơ đồ, và giữ sơ đồ đồng bộ với các feature được tham chiếu.
- Không cần sơ đồ cho spec không có luồng xuyên service/boundary hoặc khi sơ đồ không làm rõ thêm quan hệ giữa các feature.
- Viết ngắn gọn nhưng đầy đủ điều kiện, trường hợp lỗi, ranh giới và acceptance detail cần thiết để implement/verify. Không lặp contract giữa Overview, sơ đồ, feature hoặc ghi chú.

**Feature và các bước**
- Mỗi feature bắt đầu bằng heading có ID, sau đó ghi `Loại`, `Thẻ` và `Trạng thái`.
- Dùng các bước ngắn bằng ngôn ngữ nghiệp vụ để định nghĩa feature. Nêu rõ ai làm gì và kết quả tiếp theo; mỗi bước một hành động hoặc kết quả.
- Ưu tiên một câu ngắn, khoảng 15 từ hoặc ít hơn cho mỗi bước. Nếu ý dài, tách thành nhiều bước; không nén cả feature thành một đoạn văn.
- Viết nhánh bằng câu tự nhiên: `Nếu email đã được dùng, NCP yêu cầu chứng minh account.` Không dùng cú pháp `IF/ELSE`.
- Viết lặp bằng câu tự nhiên: `Với mỗi service call, nhóm ghi caller, API đích và credential.` Không dùng cú pháp `FOR EACH/END`.
- Nêu các nhánh quan trọng, kết quả lỗi và side effect bị cấm. Có thể thêm detail cho schema, API, state, UI hoặc design ngay trong feature đó.
- Với `deliverable`, các bước mô tả việc cần làm và kết quả/artifact bàn giao; không ép thành runtime flow.
- Với `invariant`, `config` hoặc `nfr`, ghi điều kiện phải giữ, nguồn giá trị hoặc ngưỡng cần đạt; không tạo bước runtime giả tạo.
- Có thể thêm `Design / implementation`, `Delivery / rollout`, `Dependencies / risks` trong feature khi cần. Đây là detail hỗ trợ review, không ghi đè contract.

**Tiêu đề, `Status`, `Audited`**
- `Status: Approved` khi mọi feature chưa `Removed` đều có contract `Approved`,
  không còn dòng trong `Proposed changes`, không còn `[Gating]`; trường hợp khác
  là `Draft`. Status của file phản ánh toàn bộ scope, không xóa hiệu lực của
  feature đã `Approved` riêng lẻ.
- `Audited: <ngày> by <người duyệt>`. Chỉ task owner quyết định duyệt để người
  sở hữu contract kiểm soát thay đổi. Approval phải xác định proposal/requirement
  và nội dung được duyệt trong hội thoại hoặc PR/commit; yêu cầu chung khi chưa có
  proposal cụ thể không tự là approval. AI được ghi lại quyết định đã có và cập
  nhật trạng thái, không tự duyệt hoặc hỏi lại khi scope không đổi. Ghi nguồn xác
  nhận và người duyệt trong hồ sơ task hoặc PR/commit khi có; không tự tạo
  commit/PR để ghi approval.

**Scope**
- Tối đa 2 câu, nêu rõ phần thuộc và không thuộc scope.
- Một file tương ứng một scope contract, không phải một feature. Gộp nhiều feature vào cùng file khi chúng góp phần vào cùng outcome/workflow, dùng chung state/invariant, hoặc cần được review và duyệt cùng nhau.
- Tạo file mới chỉ khi outcome là contract riêng có thể review, duyệt, implement và verify độc lập mà không làm spec hiện có thiếu hoặc mâu thuẫn. Có thể thêm feature vào spec hiện có khi feature mới thuộc cùng scope.
- Không tách file chỉ vì có nhiều feature, component bị ảnh hưởng hoặc implementation ở nhiều PR. Không gộp hai outcome chỉ vì chúng thuộc cùng domain folder.
- Domain folder chỉ là nhóm điều hướng; không quyết định số lượng spec hay ranh giới contract.

**Loại**
- `Loại` xác định acceptance detail cần có. Ghi loại tại từng feature, ví dụ `**Loại:** behavior · **Thẻ:** - · **Trạng thái:** Proposed · Todo`:

| Loại | Nội dung | Khối chi tiết (khi cần) |
|---|---|---|
| `behavior` | Trigger, hành vi, đường lỗi | `Điều kiện \| Kết quả` |
| `schema` | Cấu trúc dữ liệu | `Field \| Kiểu \| Ràng buộc` |
| `api` | Endpoint, interface | `Request \| Response \| Status` |
| `state` | Máy trạng thái | `Từ \| Sự kiện \| Sang` |
| `invariant` | Điều kiện luôn giữ | - |
| `config` | Giá trị hằng, kèm nguồn | - |
| `nfr` | Ngưỡng hiệu năng, bảo mật, sẵn sàng | Ngưỡng và điều kiện đo |
| `ui` | Hiển thị, tương tác | Bố cục hoặc mockup |
| `deliverable` | Tài liệu, phân tích, artifact hoặc kết quả cần bàn giao | Output và tiêu chí chấp nhận |

- `Thẻ` (không có thì ghi `-`) gắn quy tắc bắt buộc:

| Thẻ | Bắt buộc thêm |
|---|---|
| `read-only` | Check xác nhận không ghi, không xóa gì |
| `secret` | Check xác nhận secret chỉ ra qua kênh nêu trong contract cho đối tượng được phép, và không xuất hiện trong log, lỗi, output khác |
| `delete` | Yêu cầu nêu phạm vi xóa; check xác nhận ngoài phạm vi không bị xóa |
| `ext-write` | Yêu cầu nêu hành vi khi chạy lại và cách đối soát trước khi retry khi timeout hoặc kết quả không xác định; check xác nhận không ghi trùng |
| `concurrent` | Check dùng từ hai actor (tiến trình hoặc luồng) chạy đồng thời và xác nhận không vi phạm |

- `Trạng thái` = `<Contract> · <Triển khai>`; đặt ở từng feature.
  - `Contract`: `Proposed` (chưa từng được duyệt) · `Approved` · `Removed` (đã duyệt xóa; giữ ID, không tái sử dụng). Chỉ `Approved` là contract, kể cả khi file đang `Draft`.
  - `Triển khai`: `Todo` · `Doing` · `Done` · `Verified`. `Done`: code xong nhưng còn check chưa verified. `Verified`: mọi check của feature đã verified.

**Kiểm chứng**
- Đặt `Kiểm chứng` ngay trong feature; không tạo bảng Check toàn cục.
- Mỗi dòng xác nhận một tình huống độc lập theo dạng: `<Check ID>: <Tình huống> → <Kết quả quan sát được>. Verified: <trạng thái>`.
- Check ID dạng `<Requirement ID>-C1`, tăng số theo từng tình huống; không tái sử dụng.
- Mỗi phát biểu bắt buộc phải có check để reviewer biết cách xác nhận contract.
  `behavior` cần check cho đường thành công và lỗi; `config` cần check nhắc tới ID.
- Check xác nhận kết quả, không chỉ việc chạy command hoặc sự tồn tại của file.
  Tách check nếu chúng có thể fail vì nguyên nhân độc lập để failure chỉ rõ phần
  contract nào chưa đạt.
- Check chỉ kiểm bằng mắt (chỉ dùng cho `ui`) nêu tình huống và kết quả người xem phải xác nhận.
- `Verified`: `-` (chưa chạy) · `<ngày> · <commit>` (check lệnh đã pass) · `<ngày> · <người xem>` (check `manual`) · `Removed`.

**Detail theo loại task**
- Thêm `Design / implementation`, `Delivery / rollout`, `Dependencies / risks` hoặc detail chuyên biệt trong feature khi task cần; bỏ phần không áp dụng, không ghi `N/A`.
- Với migration, deployment, data change hoặc thay đổi có rollout, nêu thứ tự triển khai, tương thích trong giai đoạn chuyển tiếp, rollback/recovery và cách đối soát nếu có liên quan.
- Với bugfix, nêu điều kiện tái hiện, hành vi hiện tại, hành vi mong muốn và acceptance check.
- Với documentation, research hoặc task chỉ tạo artifact, dùng loại `deliverable` và ghi rõ artifact, người/đối tượng nhận và tiêu chí hoàn thành.

**Proposed changes**
- Chỉ dành cho `Change` và `Remove` feature đã `Approved`. Feature mới được định nghĩa ngay trong `Features` với trạng thái `Proposed · Todo`.

**Open questions**
- Điểm thiếu thông tin mà không hỏi được. Đánh `Gating` nếu ảnh hưởng contract.

## Nguyên tắc chung

- Viết tiếng Việt, giữ English cho thuật ngữ, tên lệnh, path, identifier. Một khái niệm một cách gọi.
- Dùng "phải / không được / chỉ". Không dùng "nên / thường / hợp lý / đúng / nhanh / cũ / mới", trừ khi nêu mốc hoặc ngưỡng.
- Mỗi ô bảng một điều kiện hoặc một hành vi. Cấu trúc nhiều thành phần đặt ở khối chi tiết.
- Giá trị, quyền, path phải có nguồn: file config cụ thể hoặc người quyết định. Không tự đoán.
- Mỗi yêu cầu định nghĩa một nơi; chỗ khác trỏ tới ID để tránh drift giữa các
  bản sao. Yêu cầu ở file khác trỏ bằng `<ID> (docs/specs/<domain>/<scope-slug>.md)`,
  không chép lại; ID được trỏ tới phải tồn tại và `Approved`.
- Contract trên ranh giới giữa hai file (endpoint, payload, format, schema dùng chung) chỉ định nghĩa ở file của bên cung cấp. File của bên dùng chỉ trỏ tới ID.
- Đặt spec theo một cấp domain: `docs/specs/<domain>/<scope-slug>.md`. `<domain>` là subsystem sở hữu contract; `<scope-slug>` mô tả outcome/capability có thể review độc lập. Cả hai dùng tiếng Anh chữ thường, số và dấu gạch ngang; mỗi phần khớp `^[a-z0-9]+(-[a-z0-9]+)*$`. Không lồng domain nhiều cấp.
- Folder domain dùng để tìm spec, không quyết định scope hoặc trạng thái duyệt. Một file có thể chứa nhiều feature cùng contract/lifecycle; tách file khi outcome có thể review và duyệt độc lập. Với spec ảnh hưởng nhiều domain, đặt file theo subsystem sở hữu contract và liên kết nó từ `docs/specs/catalog.md`; không nhân bản contract.
- Spec là contract theo scope, không phải task log: không dùng ngày, ID hoặc số thứ tự trong tên file; không đặt tên file `README`. `docs/specs/README.md` chứa quy chuẩn dùng chung, không phải spec hay catalog của một project.
- Catalog theo project nằm ở `docs/specs/catalog.md` để `sync.py` có thể cập nhật `README.md` mà không ghi đè danh mục riêng. Catalog liệt kê domain, mục đích của domain và link tới từng spec; `catalog.md` không phải contract spec.
- Khi task tạo hoặc tổ chức spec, tạo `docs/specs/catalog.md` nếu chưa có; cập nhật catalog và mọi link tới file đã thêm, chuyển hoặc đổi tên. Dùng path từ repository root trong tham chiếu, ví dụ `docs/specs/terminal/split-panes.md`.
- Spec mới dùng cấu trúc domain ở trên. Khi sửa spec legacy, giữ path hiện tại trừ khi task yêu cầu di chuyển. Không tổ chức lại spec không liên quan. Migration toàn bộ spec là task riêng; khi thực hiện, giữ nguyên contract, ID và trạng thái, đồng thời cập nhật catalog và mọi link bị ảnh hưởng. Không đưa `README.md` hoặc `catalog.md` vào domain folder.
- Prefix 3-4 chữ in hoa do người quyết định chọn, mặc định là ba chữ đầu của `<scope-slug>` sau khi bỏ dấu gạch ngang (`incremental-build` → `INC`). Prefix phải duy nhất trên toàn bộ spec; nếu trùng, người quyết định chọn prefix khác. Sau khi đã dùng trong ID, không đổi prefix.
- ID: yêu cầu `INC-001`, check `INC-001-C1`. ID không đổi, không tái dùng, kể cả dòng `Removed`.

## Thay đổi và duyệt

1. Sửa code để conform yêu cầu `Approved` (refactor, typo, bugfix): làm luôn. Behavior mong đợi thiếu hoặc mơ hồ thì dừng implementation phần bị ảnh hưởng và soạn proposal. Contract không cần mô tả thuật toán hoặc implementation detail trừ khi đó là constraint đã duyệt. Được tiếp tục điều tra read-only và phần độc lập đã được phép.
2. Thêm, xóa, đổi hành vi hoặc giá trị: feature mới được định nghĩa trong `Features` với requirement ID mới, trạng thái `Proposed · Todo`. Với feature `Approved`, **giữ nguyên contract hiện tại** và ghi đề xuất vào `Proposed changes`. Yêu cầu `Proposed` cần giá trị khác thì tạo ID khác. Chờ duyệt trước khi implement thay đổi contract; chỉ implement phần `Approved`.
3. Sau khi owner duyệt nội dung cụ thể: agent được ghi lại quyết định và cập nhật feature và trạng thái requirement; `Remove` chuyển thành `Removed`; xóa proposal tương ứng; cập nhật `Audited`; nêu người duyệt và nguồn approval trong hồ sơ task hoặc PR/commit khi có.
4. Bị từ chối: ghi lý do vào PR/commit, xóa dòng khỏi `Proposed changes`; yêu cầu `Proposed` bị từ chối thì chuyển `Removed`.
5. AI agent phải đọc spec liên quan và xác định feature/ID bị ảnh hưởng trước khi đề xuất. Proposal nêu thay đổi cụ thể, lý do và ảnh hưởng tới scope, contract hoặc check. Nếu có nhiều cách hiểu làm thay đổi behavior, scope, acceptance criteria, API/data hoặc implementation boundary, agent phải hỏi task owner; không tự chọn rồi coi là contract. Nếu chưa thể hỏi, ghi câu hỏi vào `Open questions` và đánh `[Gating]` nếu câu trả lời ảnh hưởng contract.
6. PR/commit nêu ID đã đổi và code/test/runbook cần xem lại.

## Tự kiểm

Trước khi trả, kiểm và báo kết quả:
- Đã thay nội dung minh họa bằng nội dung task; không còn ID, feature hoặc giá trị ví dụ.
- Spec mới hoặc được di chuyển trong task có path khớp `docs/specs/<domain>/<scope-slug>.md`; spec legacy ngoài scope không phải di chuyển. Prefix không trùng spec khác; kiểm tra trên các feature heading dạng `^### <PREFIX>-`.
- Catalog có link tới spec thêm hoặc di chuyển trong task; link bị ảnh hưởng trỏ tới path hiện có. Chỉ kiểm tra và tổ chức lại toàn bộ catalog/spec khi task yêu cầu migration hoặc audit toàn bộ.
- `Overview` một câu, `Scope` tối đa 2 câu; đầu file giúp người đọc nhận ra mục tiêu và outcome nhanh.
- Mỗi feature có đúng một ID ở đầu heading, metadata đầy đủ và contract được định nghĩa đúng một lần trong `Features`.
- Các bước ngắn, có actor rõ, dùng ngôn ngữ nghiệp vụ; nhánh/lặp viết tự nhiên, không dùng pseudocode.
- Mỗi phát biểu bắt buộc và giá trị `config` có check với kết quả mong đợi; feature có tag đáp ứng yêu cầu check của tag.
- Mỗi requirement ID duy nhất; mỗi check ID duy nhất và nằm trong feature sở hữu requirement ID đó; `Target ID` của `Change`/`Remove` tồn tại và đang `Approved`.
- Mọi tham chiếu sang file khác trỏ tới ID tồn tại và `Approved`; không có hai chỗ định nghĩa cùng hành vi.
- Liệt kê mọi điểm còn có thể hiểu khác nhau; điểm chưa giải quyết thì đánh `Gating`.
