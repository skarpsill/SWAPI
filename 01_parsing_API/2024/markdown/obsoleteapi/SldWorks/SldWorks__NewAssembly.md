---
title: "SldWorks::NewAssembly"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__NewAssembly.htm"
---

# SldWorks::NewAssembly

This method is obsolete and has been superseded
by[SldWorks::NewDocument](sldworksAPI.chm::/SldWorks/SldWorks__NewDocument.htm)or[SldWorks::INewDocument2](sldworksAPI.chm::/SldWorks/SldWorks__INewDocument2.htm).

Description

This method opens a new assembly. The assembly document is named automatically.

Syntax (OLE Automation)

retval = SldWorks.NewAssembly ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created assembly or NULL if
the operation fails |
| --- | --- | --- |

Syntax (COM)

status = SldWorks->INewAssembly
( &retval )

(Table)=========================================================

| Output: | (LPASSEMBLYDOC) retval | Pointer to a newly created assembly or NULL if the operation fails. |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If you want to set the document title without saving
the file, use ModelDoc2::SetTitle2.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZFileOperations$$**$$AssemblyDoc$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SldWorks\SldWorks__NewAssembly.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
