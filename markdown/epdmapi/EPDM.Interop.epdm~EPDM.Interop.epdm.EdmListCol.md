---
title: "EdmListCol Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListCol"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListCol.html"
---

# EdmListCol Structure

Contains information about a column in a file listing.

## Syntax

### Visual Basic

```vb
Public Structure EdmListCol
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmListCol : System.ValueType
```

### C++/CLI

```cpp
public value class EdmListCol : public System.ValueType
```

## Examples

struct EdmListCol{ string mbsCaption ; integer mlEdmListColFlags ; enum EdmColType meColType ; integer mlVariableID ; enum EdmVariableType meVarType ; integer mlWidth ; }

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)

[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

Also see the[IEdmSearch10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html)examples.

This structure is returned by[IEdmSearchResult6::GetCustomColumnsInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnsInfo.html).

## See Also

[EdmListCol Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListCol_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
