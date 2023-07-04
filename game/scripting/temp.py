
# board
        # x1 = 1 * scale + int(scale/2)
        # y1 = 1 * scale + int(scale/2)

        # x2 = 23 * scale + int(scale/2)
        # y2 = 23 * scale + int(scale/2)

        # p1 = Point(x1+int(scale/2),y1)
        # p2 = Point(x2-int(scale/2),y1)
        # p3 = Point(x1+int(scale/2),y2)
        # p4 = Point(x2-int(scale/2),y2)

        # q1 = Point(x1,y1+int(scale/2))
        # q2 = Point(x2,y1+int(scale/2))
        # q3 = Point(x1,y2-int(scale/2))
        # q4 = Point(x2,y2-int(scale/2))

        
        # thickness = 4

        # self._video_service.draw_line_ex(p1, p2, thickness, constants.BLACK) 
        # self._video_service.draw_line_ex(p3, p4, thickness, constants.BLACK) 
        # self._video_service.draw_line_ex(q1, q3, thickness, constants.RED) 
        # self._video_service.draw_line_ex(q2, q4, thickness, constants.RED) 
        
        # status: Actor = cast.get_first_actor(constants.STATUS_GROUP)
        # text = Text(status.get_text(),constants.FONT_FILE,alignment=constants.ALIGN_CENTER, color=status.get_color())
        # self._video_service.draw_text(text, status.get_screen_position(), status.get_color())


#bridge
        # if preview_player is not None:
        #     players.append(preview_player)

        # for player in players :
        #     thickness = 8
        #     for bridge in player.get_bridges():
        #         self._video_service.draw_line_ex( \
        #             bridge[0].get_screen_position(), \
        #             bridge[1].get_screen_position(), \
        #             thickness, \
        #             player.get_color())