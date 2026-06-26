---
title: "ModelDoc::FeatureReferenceCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureReferenceCurve.htm"
---

# ModelDoc::FeatureReferenceCurve

This
method is obsolete and has been superseded by[ModelDoc2::FeatureReferenceCurve](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FeatureReferenceCurve.htm).

Description

This methodcreate
a reference curve feature from an array of curves.

Syntax (OLE Automation)

retval = ModelDoc.FeatureReferenceCurve
( numOfCurves, baseCurves, merge, fromFileName, &errorCode )

(Table)=========================================================

| Input: | (long) numOfCurves | Number of curves from which to create the object |
| --- | --- | --- |
| Input: | (VARIANT) baseCurves | SafeArray of Dispatch pointers to the curves |
| Input: | (BOOL) merge | TRUE creates a single reference curve feature, FALSE creates a reference
curve feature for each curve in the array |
| Input: | (BSTR) fromFileName | Not used |
| Output: | (long) errorCode | Error code as defined in swFeatureError_e |
| Return: | (LPDISPATCH) retval | Dispatch pointer to ReferenceCurve Object. |

Syntax (COM)

status = ModelDoc->IFeatureReferenceCurve
( numOfCurves, baseCurves, merge, fromFileName, &errorCode, &retval
)

(Table)=========================================================

| Input: | (long)numOfCurves | Number of curves from which to create the object |
| --- | --- | --- |
| Input: | (LPCURVE)*baseCurves | Pointer to an array of curves |
| Input: | (VARIANT_BOOL) merge | TRUE creates a single reference curve feature, FALSE creates a reference
curve feature for each curve in the array |
| Input: | (BSTR) fromFileName | Not used |
| Output: | (long) errorCode | Error code as defined in swFeatureError_e |
| Output: | (LPREFERENCECURVE) retval | Pointer to ReferenceCurve object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__FeatureReferenceCurve.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
