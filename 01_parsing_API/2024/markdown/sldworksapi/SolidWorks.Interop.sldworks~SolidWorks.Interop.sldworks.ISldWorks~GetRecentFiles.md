---
title: "GetRecentFiles Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetRecentFiles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRecentFiles.html"
---

# GetRecentFiles Method (ISldWorks)

Gets a list of the most recently used files.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRecentFiles() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetRecentFiles()
```

### C#

```csharp
System.object GetRecentFiles()
```

### C++/CLI

```cpp
System.Object^ GetRecentFiles();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

List of most recently used files (see

Remarks

)

## VBA Syntax

See

[SldWorks::GetRecentFiles](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetRecentFiles.html)

.

## Examples

'----------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}Dim swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}Dim vFileArr As Variant

kadov_tag{{<spaces>}}Dim i As Long

kadov_tag{{<spaces>}}Set swApp = Application.SldWorks

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}vFileArr = swApp. GetRecentFiles

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}For i = 0 To UBound(vFileArr) Step 2

kadov_tag{{<spaces>}}Debug.Print vFileArr(i + 1) & " --> " & vFileArr(i)

kadov_tag{{<spaces>}}Next i

End Sub

'----------------------------------------

## Remarks

The list is returned in pairs of files.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For each pair, the first item is the fully qualified path to the file.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The second item is just the filename, as it appears in the most recent used list in the SOLIDWORKSFilemenu.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
