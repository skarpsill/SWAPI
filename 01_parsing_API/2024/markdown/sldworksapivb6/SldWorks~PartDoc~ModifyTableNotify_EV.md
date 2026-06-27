---
title: "ModifyTableNotify Event (PartDoc)"
project: "SOLIDWORKS Type Library"
interface: "PartDoc"
member: "ModifyTableNotify"
kind: "event"
source: "sldworksapivb6/SldWorks~PartDoc~ModifyTableNotify_EV.html"
---

# ModifyTableNotify Event (PartDoc)

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
