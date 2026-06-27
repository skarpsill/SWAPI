---
title: "AssemblyDoc::AddComponent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__AddComponent.htm"
---

# AssemblyDoc::AddComponent

This
method is obsolete and has been superseded by[AssemblyDoc::AddComponent2](AssemblyDoc__AddComponent2.htm).

Description

This
method adds the specified part or assembly to the current assembly as
a component.

Syntax
(OLE Automation)

retval
= AssemblyDoc.AddComponent ( compName, x, y, z)

(Table)=========================================================

| Input: | (BSTR)
compName | Path
name of a loaded part or assembly to add as a component (see below) |
| --- | --- | --- |
| Input: | (double)
x | X-coordinate
of the component center |
| Input: | (double)
y | Y-coordinate
of the component center |
| Input: | (double)
z | Z-coordinate
of the component center |
| Return: | (BOOL)
retval | TRUE
if the part or assembly was added |

Syntax (COM)

status
= AssemblyDoc->AddComponent ( compName, x, y, z, &retval )

(Table)=========================================================

| Input: | (BSTR)
compName | Path
name of a loaded part or assembly to add as a component (see below) |
| --- | --- | --- |
| Input: | (double)
x | X-coordinate of the component center |
| Input: | (double)
y | Y-coordinate of the component center |
| Input: | (double)
z | Z-coordinate of the component center |
| Output: | (VARIANT_BOOL)
retval | TRUE if the part or assembly was added |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The
specified file must be loaded in memory. A file is loaded into memory
when you load the file in your SolidWorks session (SldWorks::OpenDoc)
or open an assembly that already contains the file.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc_Object$$**$$ZModifyAssemblyDoc$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\AssemblyDoc\AssemblyDoc__AddComponent.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
