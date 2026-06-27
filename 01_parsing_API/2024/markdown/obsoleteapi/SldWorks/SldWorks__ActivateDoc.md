---
title: "SldWorks::ActivateDoc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__ActivateDoc.htm"
---

# SldWorks::ActivateDoc

This
method is obsolete and has been superseded by[SldWorks::ActivateDoc2](sldworksAPI.chm::/SldWorks/SldWorks__ActivateDoc2.htm).

Description

This method activates a document that has already been loaded. This
file becomes the active document, and this method returns a pointer to
that document object.

Syntax (OLE Automation)

retval = SldWorks.ActivateDoc ( Name)

(Table)=========================================================

| Input: | (BSTR) Name | Name of document |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, the document or NULL if the operation fails |

Syntax (COM)

status = SldWorks->IActivateDoc
( Name, &retval )

(Table)=========================================================

| Input: | (BSTR) Name | Name of document |
| --- | --- | --- |
| Output: | (LPMODELDOC) retval | Pointer to the document or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you do not specify a file extension in the Name parameter, then SolidWorks
activates the document based strictly on its name and ignores the file
extension. This may cause problems if you have two different document
types with the same name loaded , for example, 12345.sldprt and 12345.sldasm.
If you do not specify the file extension in your call to this method,
then you cannot be sure which document will be activated. To avoid this
problem, you can specify the file extension in the Name parameter or you
can check the document type after it is activated using ModelDoc2::GetType.

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
<param name="Items" value="SldWorks_Object$$**$$ZFileOperations$$**$$ZGetModelDoc$$**$$ZGetPartD$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__ActivateDoc.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Save As Example$$**$$SolidWorks_Visible_or_BackGround_Example$$**$$Close_Document_Example$$**$$Open_Assembly_Component_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__ActivateDoc.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
