---
title: "IExportToDWG2 Method (PartDoc)"
project: "SOLIDWORKS Type Library"
interface: "PartDoc"
member: "IExportToDWG2"
kind: "method"
source: "sldworksapivb6/SldWorks~PartDoc~IExportToDWG2.html"
---

# IExportToDWG2 Method (PartDoc)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function IExportToDWG2( _
   ByVal FilePath As String, _
   ByVal ModelName As String, _
   ByVal Action As Long, _
   ByVal ExportToSingleFile As Boolean, _
   ByRef Alignment As Double, _
   ByVal IsXDirFlipped As Boolean, _
   ByVal IsYDirFlipped As Boolean, _
   ByVal SheetMetalOptions As Long, _
   ByVal ViewsCount As Long, _
   ByRef Views As String _
) As Boolean
```
