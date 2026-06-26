---
title: "IExportToDWG Method (PartDoc)"
project: "SOLIDWORKS Type Library"
interface: "PartDoc"
member: "IExportToDWG"
kind: "method"
source: "sldworksapivb6/SldWorks~PartDoc~IExportToDWG.html"
---

# IExportToDWG Method (PartDoc)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function IExportToDWG( _
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
