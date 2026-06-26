---
title: "ICheckInterferenceCount3 Method (Modeler)"
project: "SOLIDWORKS Type Library"
interface: "Modeler"
member: "ICheckInterferenceCount3"
kind: "method"
source: "sldworksapivb6/SldWorks~Modeler~ICheckInterferenceCount3.html"
---

# ICheckInterferenceCount3 Method (Modeler)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function ICheckInterferenceCount3( _
   ByVal NumOfTargetBodies As Long, _
   ByVal TargetBodies As Body2, _
   ByVal NumOfToolBodies As Long, _
   ByVal ToolBodies As Body2, _
   ByVal Options As Long, _
   ByRef NumBody1InterferedFaceArray As Long, _
   ByRef NumBody2InterferedFaceArray As Long, _
   ByRef NumIntersectedBodyArray As Long _
) As Boolean
```
