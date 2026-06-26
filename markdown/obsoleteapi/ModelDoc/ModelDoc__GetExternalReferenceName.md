---
title: "ModelDoc::GetExternalReferenceName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetExternalReferenceName.htm"
---

# ModelDoc::GetExternalReferenceName

This
method is obsolete and has been superseded by[ModelDoc2::GetExternalReferenceName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetExternalReferenceName.htm).

Description

This method returns the name of the externally
referenced document if a joined or mirrored part. The full path of the
externally referenced document is returned.

Syntax (OLE Automation)

retval = ModelDoc.GetExternalReferenceName
( )

(Table)=========================================================

| Return: | (BSTR) retval | Full path of referenced document or NULL |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetExternalReferenceName
( &retval )

(Table)=========================================================

| Output: | (BSTR) retval | Full path of referenced document or NULL |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If ModelDoc does not have an externally referenced document, a null
string is returned.

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
<param name="Items" value="ModelDoc_Object$$**$$ZReferences$$**$$ZGetInfoModelDoc$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetExternalReferenceName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
