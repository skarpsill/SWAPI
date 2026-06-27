---
title: "Modeler::IImprintingFacesCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__IImprintingFacesCount.htm"
---

# Modeler::IImprintingFacesCount

This
method is obsolete and has been superceded by[Modeler::IImprintingFacesCount2](sldworksAPI.chm::/Modeler/Modeler__IImprintingFacesCount2.htm).

Description

This method returns the number of imprinted
edges and vertices

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Modeler->IImprintingFacesCount ( nTargetFaces,
*targetFaceArray, nToolFaces, *toolFaceArray, options, *nTargetEdges,
*ntoolEdges, *ntargetVertices, *toolVertices, *retval )

(Table)=========================================================

| Input: | (long) nTargetFaces | Number of faces in the target body |
| --- | --- | --- |
| Input: | (LPFACE) *targetFaceArray | List of the faces that describe the target body |
| Input: | (long) nToolFaces | Number of faces in the tool body |
| Input: | (LPFACE) *toolFaceArray | List of the faces that describe the tool body |
| Input: | (long) options | Options for this operation as defined in swImprintingFacesOpts_e |
| Output: | (long) *nTargetEdges | Number of edges returned from this operation |
| Output: | (long) *ntoolEdges | Number of tool edges returned from this operation |
| Output: | (long) *ntargetVertices | Number of target vertices returned from this
operation |
| Output: | (long) *toolVertices | Number of tool vertices returned from this operation |
| Output: | (VARIANT_BOOL) *retval | TRUE if the operation is successful, FALSE otherwise |
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__IImprintingFacesCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="Modeler_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__IImprintingFacesCount.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
