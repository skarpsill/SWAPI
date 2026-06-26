---
title: "EdmGetVarData Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetVarData"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetVarData.html"
---

# EdmGetVarData Structure

Contains extra file information.

## Syntax

### Visual Basic

```vb
Public Structure EdmGetVarData
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmGetVarData : System.ValueType
```

### C++/CLI

```cpp
public value class EdmGetVarData : public System.ValueType
```

## Examples

struct EdmGetVarData{ integer mlVersion ; integer mlLatestVersion ; string mbsRevision ; string mbsState ; string mbsWorkflow ; string mbsCategory ; integer mlDateFmt ; integer mlEdmGetVarDataFlags ; };

## Examples

[Get File Variable Data (VB.NET)](Get_File_Variable_Data_Example_VBNET.htm)

[Get File Variable Data (C#)](Get_File_Variable_Data_Example_CSharp.htm)

## Remarks

Returned by

[IEdmEnumeratorVariable7::GetVersionVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7~GetVersionVars.html)

.

## See Also

[EdmGetVarData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetVarData_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
