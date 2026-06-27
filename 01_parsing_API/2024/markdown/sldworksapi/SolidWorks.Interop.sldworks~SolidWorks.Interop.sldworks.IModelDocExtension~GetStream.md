---
title: "GetStream Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetStream"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetStream.html"
---

# GetStream Method (IModelDocExtension)

Gets the handle for the specified stream.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStream( _
   ByVal StreamType As System.Integer, _
   ByRef ReadOnly As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim StreamType As System.Integer
Dim ReadOnly As System.Boolean
Dim value As System.Object

value = instance.GetStream(StreamType, ReadOnly)
```

### C#

```csharp
System.object GetStream(
   System.int StreamType,
   out System.bool ReadOnly
)
```

### C++/CLI

```cpp
System.Object^ GetStream(
   System.int StreamType,
   [Out] System.bool ReadOnly
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `StreamType`: 1 = material stream
- `ReadOnly`: True if the stream is read-only, false if not

### Return Value

Pointer to the IUnknown interface for this stream

## VBA Syntax

See

[ModelDocExtension::GetStream](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetStream.html)

.

## Remarks

To release the stream, call[IModelDocExtension::ReleaseStream](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ReleaseStream.html).

**VB Example**

This example illustrates attaching an XML document to a stream, and then releasing the stream.

Dim swApp As Object

Sub main()

Set swApp = Application.SldWorks

Dim docext As SldWorks.ModelDocExtension

Set docext = swApp.ActiveDoc.Extension

Dim xmldoc As MSXML2.DOMDocument

Set xmldoc = CreateObject("MSXML2.DOMDocument")

Dim stat As Boolean

Dim stream

Set stream = docext. GetStream (1, stat)

xmldoc.Load (stream)

docext. ReleaseStream (1)

xmldoc.Save ("C:\temp\xmlmat.xml")

End Sub

**C++ Example**

//--------

kadov_tag{{<spaces>}}CComPtr<IModelDocExtension> ext;

kadov_tag{{<spaces>}}m_iModelDoc2->get_Extension(&ext);

kadov_tag{{<spaces>}}LPSTREAM stream = NULL;

kadov_tag{{<spaces>}}VARIANT_BOOL access = 0;

kadov_tag{{<spaces>}}ext-> IGetStream (1, &access, &stream);

kadov_tag{{<spaces>}}// Your code

kadov_tag{{<spaces>}}if (stream)

kadov_tag{{<spaces>}}{

kadov_tag{{<spaces>}}VARIANT_BOOL status;

kadov_tag{{<spaces>}}ext-> IReleaseStream (1, &status);

kadov_tag{{<spaces>}}stream->Release();

kadov_tag{{<spaces>}}}

kadov_tag{{<spaces>}}//--------

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
