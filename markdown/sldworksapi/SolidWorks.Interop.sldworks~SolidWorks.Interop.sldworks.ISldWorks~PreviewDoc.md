---
title: "PreviewDoc Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "PreviewDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDoc.html"
---

# PreviewDoc Method (ISldWorks)

Displays a preview of a document to the specified window.

## Syntax

### Visual Basic (Declaration)

```vb
Function PreviewDoc( _
   ByRef HWnd As System.Integer, _
   ByVal FullName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim HWnd As System.Integer
Dim FullName As System.String
Dim value As System.Boolean

value = instance.PreviewDoc(HWnd, FullName)
```

### C#

```csharp
System.bool PreviewDoc(
   ref System.int HWnd,
   System.string FullName
)
```

### C++/CLI

```cpp
System.bool PreviewDoc(
   System.int% HWnd,
   System.String^ FullName
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `HWnd`: Window handle where you want the preview bitmap to display; this pointer is not valid across processes; therefore, this method only works if your application is implemented as a DLL
- `FullName`: Full path name of document to preview

### Return Value

True if successful, false if not

## VBA Syntax

See

[SldWorks::PreviewDoc](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~PreviewDoc.html)

.

## Remarks

If your application must be x64 compatible, then use[ISldWorks::PreviewDocx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~PreviewDocx64.html).

The bitmap is stored with the fixed size shown with the interactive SOLIDWORKS preview option. If your window is a different size, then the image is scaled appropriately. If scaling is needed, then shaded images may not be as crisp as the original.

This method works well in the WM_PAINT Windows Message handler. If used in WM_ONINITDIALOG the dialog only displays the preview for a brief moment. The reason is that the dialog should be initialized completely before calling SldWorks::PreviewDoc.

C++ programmers can also access this bitmap image from outside SOLIDWORKS. The bitmap was written with CArchive::Write( ) and is found in the Preview node in SOLIDWORKS part, assembly and drawing files. The format of the Preview node is as follows: DWORD (data size) followed by continues chunk of memory of that size (data). The data being read can be cast to LPBITMAPINFO, which has all of the information required to display the bitmap. You may want to use StretchDIBits() when displaying your image of the bitmap.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)

[ISldWorks::GetPreviewBitmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmap.html)
