---
title: "ModifyTableNotify Event (DrawingDoc)"
project: "SOLIDWORKS Type Library"
interface: "DrawingDoc"
member: "ModifyTableNotify"
kind: "event"
source: "sldworksapivb6/SldWorks~DrawingDoc~ModifyTableNotify_EV.html"
---

# ModifyTableNotify Event (DrawingDoc)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Event ModifyTableNotify( _
   ByVal TableAnnotation As TableAnnotation, _
   ByVal TableType As Long, _
   ByVal reason As Long, _
   ByVal RowInfo As Long, _
   ByVal ColumnInfo As Long, _
   ByVal DataInfo As String _
)
```
