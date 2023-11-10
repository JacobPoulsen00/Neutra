import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { alpha } from '@mui/material/styles';

import ReactSpeedometer from "react-d3-speedometer"

import { CircularProgress, Typography, Stack, Card, Button, TextField, Box } from '@mui/material';

export default function AppAnalyze({ placeholder, submit, welcome, ...other }) {
  const [articleURL, setArticleURL] = useState('');
  const [sentimentValue, setSentimentValue] = useState(20);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: articleURL }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const result = await response.json();
      
      console.log(result.data)
      if (!Number.isNaN(+result.data)) {
        setSentimentValue(0);
      }
      setSentimentValue(result.data);
    } catch (error) {
      setSentimentValue(0);
      console.log('Error analyzing the article. Please try again.')
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card {...other} sx={{bgcolor: (theme) => alpha(theme.palette.primary.main, 0.16)}}>
      <Stack direction="row" sx={{ px: 6, py: 6 }} spacing={10} >
        <Stack spacing={5}>
          <Stack spacing={1}>
            <Typography variant="h4" >
            {welcome}   
            </Typography>
            <Typography variant="body2" sx={{width:2/3}}>
            If you are going to use a passage of Lorem Ipsum, you need to be sure there isnt anything
            </Typography>
          </Stack>

          <Stack direction="row" spacing={2}>
              <TextField
                fullWidth
                placeholder={placeholder}
                variant="outlined"
                value={articleURL}
                hiddenLabel
                aria-label="UrlAnalyse"
                sx={{ 
                  '& .MuiOutlinedInput-input': { 
                    padding: '14px', 
                    fontSize: '0.875rem',
                  },
                  "& .MuiOutlinedInput-root": {
                    bgcolor: (theme) => (theme.palette.common.white)
                  }
                }}
                onChange={e => setArticleURL(e.target.value)}
              />
              <Button 
                variant="contained" 
                color='primary'
                disabled={loading}
                endIcon={loading ? <CircularProgress size={20} /> : null}
                sx={{ 
                  padding: '0px 22px',
                  fontSize: '0.875rem',
                  minHeight: '48px'
                }}
                onClick={handleSubmit}>
                {loading ? 'Loading...' : submit}
              </Button>
          </Stack>
        </Stack>
        <Box display="flex" justifyContent="center" alignItems="center" height="100%">
          <ReactSpeedometer
                          maxValue={500}
                          value={sentimentValue}
                          valueFormat="d"
                          segments={5}
                          startColor="#a3be8c"
                          endColor="#bf616a"
                          needleColor="#bf616a"
                          textColor="black"
                          width={300}
                          height={155}
                          forceRender
                          svgAriaLabel="Bias speedometer"
                      />
        </Box>
      </Stack>
    </Card>
  );
}

AppAnalyze.propTypes = {
  placeholder: PropTypes.string.isRequired,
  welcome: PropTypes.object,
  submit: PropTypes.string,
};
